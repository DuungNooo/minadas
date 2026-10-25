package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import java.util.*;

/** Four authored conversations per companion, unlocked by play rather than repeated gifts. */
public final class Bonds {
    public record Scene(String title,String body,String first,String second,String requirement,int step) {}
    private static final Map<String,List<Scene>> STORIES=Map.of(
        "adeline",List.of(
            new Scene("빈 의자","아델린은 정전 뒤에도 입학 명부를 정리한다. 실종자 이름 옆에는 빈칸이 남아 있다. ‘돌아올 자리까지 지워도 되는 걸까요?’","돌아올 자리를 남기자","찾으러 갈 사람부터 정하자","blackout",6),
            new Scene("부치지 못한 편지","수도에서 돌아온 아델린은 가족에게 안전하다고 쓰려다 멈춘다. 거짓말을 하지 않고도 안심시킬 수 있을까.","함께 버티고 있다고 쓰자","두려움도 솔직하게 적자","capital_refuge",6),
            new Scene("명부 밖의 이름","연맹은 피해자들을 숫자로 기록했다. 아델린은 한 사람씩 이름을 되찾으려 한다.","기록을 공개하자","가족에게 먼저 전하자","buried_lab",6),
            new Scene("당신의 자리","‘영웅의 자리 말고, 지쳤을 때 돌아올 의자를 준비해 둘게요.’ 아델린이 마지막으로 당신의 이름을 적는다.","함께 다음 입학생을 맞자","다녀올 때마다 소식을 전하자","castle_memory",6)),
        "kyle",List.of(
            new Scene("무딘 검","카일의 훈련검에는 오래된 금이 있다. ‘잘 싸우는 것보다 무사히 돌아오는 법을 먼저 가르쳤어야 했지.’","살아 돌아오는 훈련을 하자","잊지 않되 자신을 탓하지 말자","blackout",6),
            new Scene("뒤돌아서는 용기","광산 구조 기록을 읽은 카일이 묻는다. ‘이길 수 없는 싸움에서 물러나는 것도 실력일까?’","지킬 사람이 있으면 그렇다","다시 싸울 기회를 남기는 일이다","mine_depths",6),
            new Scene("다음 수업","카일은 구조와 엄호를 새 교과에 넣으려 한다. 혼자 가장 강한 학생을 뽑던 시험도 바꾸고 싶다고 한다.","협동 평가를 넣자","실패한 뒤 판단도 평가하자","capital_refuge",6),
            new Scene("훈련장의 불","‘다음 학생들에게도 네가 배운 걸 전해 줘.’ 카일은 당신에게 강사의 자리가 아니라 동료의 자리를 내준다.","함께 가르치겠다","현장에서 배운 것을 보내겠다","castle_memory",6)),
        "seraphine",List.of(
            new Scene("남은 붕대","세라핀은 치료 재료를 세며 구조 대상의 이름을 되뇐다. ‘모두를 살리고 싶다는 말은 너무 쉬워요.’","먼저 당신도 쉬어야 한다","혼자 결정하지 않도록 돕겠다","canal_rescue",4),
            new Scene("빈 침대","치료소를 지켜낸 뒤에도 그녀는 잠들지 못한다. 구한 사람보다 구하지 못할 뻔한 사람이 자꾸 떠오른다.","구해낸 사람들의 소식을 전하자","오늘은 곁에서 함께 쉬자","capital_refuge",6),
            new Scene("적의 손","남부에서 구한 포로가 치료를 거부한다. 자신은 도움받을 자격이 없다고 말한다.","치료는 보상이 아니라고 말하자","먼저 그의 이야기를 듣자","south_forge",4),
            new Scene("내일의 약속","‘상처가 사라져야만 살아갈 수 있는 건 아니었네요.’ 세라핀은 치료소 문에 새 간판을 건다.","누구에게나 열린 문으로 만들자","치료사들도 쉴 곳을 만들자","castle_memory",6)),
        "irina",List.of(
            new Scene("금이 간 표본","이리나는 부서진 표본보다 실험을 중단하지 못한 자신을 탓한다. 연구가 사람보다 중요해진 순간을 놓쳤다고 한다.","중단한 판단도 연구다","다음 안전 규칙을 함께 만들자","mine_depths",6),
            new Scene("검은 배관","숲의 배관을 보고 이리나는 자신의 계산식과 닮았음을 알아본다. 올바른 식도 잘못 쓰일 수 있었다.","사용 목적까지 기록하자","피해를 먼저 복구하자","forest_heart",6),
            new Scene("연구의 주인","아카데미는 연구를 비밀로 남기고 싶어 한다. 이리나는 공개 검증 없이는 같은 일이 반복된다고 말한다.","검증 가능한 기록을 남기자","피해자의 의견을 먼저 듣자","buried_lab",6),
            new Scene("다음 탐사","‘이번엔 혼자 결정하지 않을게요.’ 이리나는 새 연구 계획서의 공동 연구자 칸을 비워 둔다.","함께 이름을 적자","현장 사람들의 이름도 넣자","castle_memory",6)),
        "noah",List.of(
            new Scene("서가의 먼지","노아는 틀린 기록도 버리지 않는다. ‘무엇을 숨겼는지 알아야 진실에 다가갈 수 있으니까요.’","지워진 부분부터 보자","서로 다른 기록을 비교하자","blackout",6),
            new Scene("정답 없는 주석","봉인 연구는 사실이지만 완전한 진실은 아니었다. 노아는 자신이 학생들에게 무엇을 가르쳤는지 되묻는다.","수정한 이유도 남기자","먼저 학생들에게 설명하자","buried_lab",6),
            new Scene("교수의 증언","노아는 교수에게 연구의 공로만큼 책임도 기록하겠다고 말한다. 교수는 조용히 고개를 끄덕인다.","피해자의 증언을 함께 싣자","원본을 누구나 읽게 하자","cult_hideout",6),
            new Scene("첫 장","‘새 봉인 기록의 첫 장에는 왕과 연맹이 아니라 살아남은 사람들의 이름을 적겠습니다.’","빠진 이름을 함께 찾자","다음 세대가 고칠 여백도 남기자","castle_memory",6)),
        "riana",List.of(
            new Scene("틀린 지도","리아나의 지도는 정확했지만 얼어붙은 물길은 달랐다. ‘지도에 없는 변화까지 볼 줄 알아야 했어요.’","현장의 말을 먼저 듣자","변화를 지도에 함께 남기자","canal_rescue",6),
            new Scene("신호를 기다리는 밤","평원의 마지막 신호를 들은 리아나는 구조대가 돌아올 때까지 지도를 접지 않는다.","함께 기다리자","귀환 경로를 한 번 더 살피자","storm_signal",6),
            new Scene("돌아오는 길","북부에서 길은 눈 속에 사라졌다. 리아나는 사람이 남긴 불빛을 새로운 표지로 그린다.","구조 표지를 늘리자","누구나 읽을 지도를 만들자","north_watch",6),
            new Scene("빈 곳의 의미","‘모르는 곳은 지도의 실패가 아니라 앞으로 만날 곳이더군요.’ 리아나는 다음 여정의 빈 종이를 편다.","다음 길을 함께 찾자","먼저 돌아갈 곳을 표시하자","castle_memory",6)),
        "claude",List.of(
            new Scene("살아남은 사람","클라우드는 동부의 이름들을 기억한다. 자신만 살아남았다는 말 뒤에는 긴 침묵이 이어진다.","살아남은 이유를 지금 정하자","말하지 않아도 곁에 있겠다","east_garden",2),
            new Scene("새싹","약초원을 복구한 뒤 클라우드는 작은 화분을 받았다. ‘키우는 법은 모른다’면서도 가장 안전한 곳에 둔다.","같이 배워 보자","돌아올 이유가 하나 늘었다","east_garden",6),
            new Scene("등을 맡기는 일","혼자 움직이던 클라우드가 처음으로 뒤를 부탁한다. 명령이 아니라 요청이었다.","맡겨도 된다","나도 당신에게 맡기겠다","south_forge",6),
            new Scene("돌아갈 곳","‘이번에는 살아남는 것만으로 끝내지 않겠다.’ 클라우드는 화분을 아카데미 창가에 옮긴다.","여기서 새 삶을 시작하자","가끔은 다시 함께 떠나자","castle_memory",6))
    );
    public static void add(ServerPlayer p,Entity npc,String id,List<Menus.Option> options){
        if(STORIES.containsKey(id))options.add(new Menus.Option("인연 이야기",()->show(p,npc,id)));
    }
    private static void show(ServerPlayer p,Entity npc,String id){
        var scenes=STORIES.get(id);int stage=Math.clamp(Progress.data(p).getInt("bond_scene_"+id),0,4);
        if(stage>=4){Menus.show(p,Content.NPCS.get(id).name(),"함께한 네 사건이 모두 기록되었습니다. 당신의 선택은 인연 기록에 남습니다.\n\n"+scenes.getLast().body(),npc,List.of(new Menus.Option("돌아가기",()->Menus.npc(p,npc))));return;}
        var scene=scenes.get(stage);var chapter=Expeditions.chapter(scene.requirement());
        if(Expeditions.progress(p,chapter)<scene.step()){
            Menus.show(p,"인연 이야기 · "+(stage+1)+" / 4","다음 이야기: "+scene.title()+"\n\n먼저 「"+chapter.title()+"」의 "+scene.step()+"번째 목표까지 진행하세요. 선물을 반복할 필요는 없습니다.",npc,List.of(new Menus.Option("돌아가기",()->Menus.npc(p,npc))));return;
        }
        Menus.show(p,scene.title(),scene.body(),npc,List.of(new Menus.Option(scene.first(),()->choose(p,npc,id,stage,0)),new Menus.Option(scene.second(),()->choose(p,npc,id,stage,1))));
    }
    private static void choose(ServerPlayer p,Entity npc,String id,int expected,int choice){
        var d=Progress.data(p);if(d.getInt("bond_scene_"+id)!=expected)return;
        d.putInt("bond_choice_"+id+"_"+expected,choice);d.putInt("bond_scene_"+id,expected+1);
        String key="fantasia_affection_"+id;d.putInt(key,Math.min(100,d.getInt(key)+20));
        if(d.getInt(key)>=80)Progress.grant(p,"bond/"+id);
        show(p,npc,id);
    }
    public static int deepBonds(ServerPlayer p){return (int)STORIES.keySet().stream().filter(id->Progress.data(p).getInt("fantasia_affection_"+id)>=80).count();}
    private Bonds(){}
}
