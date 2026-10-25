package kr.fantasia.campaign.client;

import kr.fantasia.campaign.Packets;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.components.Tooltip;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.network.chat.Component;
import net.minecraft.util.FormattedCharSequence;
import net.neoforged.neoforge.network.PacketDistributor;
import java.util.List;

public final class DialogueScreen extends Screen {
    private final Packets.View view;
    private int page=0,scroll=0,left,top,panelWidth,panelHeight,bodyHeight,perPage;
    private boolean submitted=false;
    private List<FormattedCharSequence> lines=List.of();
    public DialogueScreen(Packets.View view){super(Component.literal(view.title()));this.view=view;}
    @Override protected void init(){
        panelWidth=Math.min(540,width-20);panelHeight=Math.min(390,height-16);left=(width-panelWidth)/2;top=(height-panelHeight)/2;
        bodyHeight=Math.max(40,panelHeight/2-20);perPage=Math.max(2,Math.min(6,(panelHeight-bodyHeight-100)/24*2));
        lines=font.split(Component.literal(view.body()),panelWidth-36);
        page=Math.clamp(page,0,Math.max(0,(view.buttons().size()-1)/perPage));
        int y=top+bodyHeight+48;
        for(int i=page*perPage;i<Math.min(view.buttons().size(),(page+1)*perPage);i++){
            int index=i,slot=i-page*perPage;
            String value=view.buttons().get(i);
            Component label=value.startsWith("translate:")?Component.translatable(value.substring(10)):Component.literal(value);
            addRenderableWidget(Button.builder(label,b->{if(!submitted){submitted=true;PacketDistributor.sendToServer(new Packets.Click(view.token(),index));minecraft.setScreen(null);}})
                .bounds(left+16+(slot%2)*(panelWidth/2-8),y+(slot/2)*24,panelWidth/2-24,20).tooltip(Tooltip.create(label)).build());
        }
        int pages=Math.max(1,(view.buttons().size()+perPage-1)/perPage);
        if(pages>1){
            var prev=addRenderableWidget(Button.builder(Component.literal("이전"),b->{page--;rebuildWidgets();}).bounds(left+16,top+panelHeight-30,55,20).build());prev.active=page>0;
            var next=addRenderableWidget(Button.builder(Component.literal("다음"),b->{page++;rebuildWidgets();}).bounds(left+78,top+panelHeight-30,55,20).build());next.active=page+1<pages;
        }
        addRenderableWidget(Button.builder(Component.literal("닫기"),b->onClose()).bounds(left+panelWidth-70,top+panelHeight-30,54,20).build());
    }
    @Override public void render(GuiGraphics g,int mouseX,int mouseY,float partialTick){
        g.fill(0,0,width,height,0xB0101522);g.fill(left,top,left+panelWidth,top+panelHeight,0xF0192235);
        g.fill(left,top,left+panelWidth,top+3,0xFFD7B46A);
        g.drawString(font,font.plainSubstrByWidth(title.getString(),panelWidth-32),left+16,top+14,0xFFE4C682,false);
        g.enableScissor(left+16,top+36,left+panelWidth-16,top+36+bodyHeight);
        int lineHeight=font.lineHeight+3;
        for(int i=0;i<lines.size();i++)g.drawString(font,lines.get(i),left+18,top+38+i*lineHeight-scroll,0xFFE7ECF3,false);
        g.disableScissor();
        if(lines.size()*lineHeight>bodyHeight)g.drawString(font,"휠로 본문 스크롤",left+16,top+bodyHeight+36,0xFF95ABC4,false);
        if(view.buttons().size()>perPage)g.drawString(font,(page+1)+" / "+((view.buttons().size()+perPage-1)/perPage),left+145,top+panelHeight-24,0xFF95ABC4,false);
        super.render(g,mouseX,mouseY,partialTick);
    }
    @Override public boolean mouseScrolled(double x,double y,double dx,double dy){scroll=Math.clamp(scroll-(int)(dy*18),0,Math.max(0,lines.size()*(font.lineHeight+3)-bodyHeight));return true;}
    @Override public void onClose(){if(!submitted)PacketDistributor.sendToServer(new Packets.Click(view.token(),-1));super.onClose();}
    @Override public boolean isPauseScreen(){return false;}
}
