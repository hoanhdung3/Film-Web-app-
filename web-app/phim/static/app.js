function alreadyloaded(){
//----------------------------------------------------------------username(JQuery)
    $(document).ready(function(){
        $('.username').parent('div').addClass('has-child');
    });
//----------------------------------------------------------------scroll recommendations
    var track= document.querySelector('.recommendations__track');
    var first_card= document.querySelector('.first-one');
    var amount_to_move= first_card.getBoundingClientRect().width*4;
    console.log(amount_to_move/4);

    var right_button=document.querySelector('.button-right-recommendations');
    var left_button= document.querySelector('.button-left-recommendations');


    i=0; 
    var move_to_the_right_recommendations= (track)=> {
        for(i=i; i<=0; i++){
            if(i>0)
                return;
            else
                i++;
            track.style.transform= 'translateX(-' + (amount_to_move+99)*i+ 'px)';
            amount_aleady_moved= (amount_to_move+99)*i;
            console.log(i);
            return;
        }
    }

    var move_to_the_left_recommendations= (track)=> {
        for(i=i; i>0; i--){
            if(i<1)
                return;
            else
                i--;
            track.style.transform= 'translateX(-' + (amount_to_move+99)*i+ 'px)';
            amount_aleady_moved= (amount_to_move+99)*i;
            console.log(i);       
            return;
        }
    }
    right_button.addEventListener('click', e=>{
        move_to_the_right_recommendations(track); 
        hide_button_recommendations(right_button, left_button, amount_aleady_moved);
    });

    left_button.addEventListener('click', e=>{
        move_to_the_left_recommendations(track);
        hide_button_recommendations(right_button, left_button, amount_aleady_moved);
    });

    var hide_button_recommendations= (right_button, left_button, amount_aleady_moved)=>{
        if(amount_aleady_moved===(amount_to_move+99)){
            right_button.classList.add('be-hidden');
            left_button.classList.remove('be-hidden');
        }
        else{
            right_button.classList.remove('be-hidden');
            left_button.classList.add('be-hidden');
        }

    }
    
    // setInterval

    // var auto_move= (right_button, left_button, track, amount_to_move)=>{
    //     track.style.transform= 'translateX(-' + (amount_to_move+99) + 'px)';
       
    
    //     left_button.addEventListener('click', e=>{
    //         track.style.transform= 'translateX(' +0 + 'px)';
    //     });
    // }

    //-------------------------------------------------------------------------Blockbusters

    var right_button_block= document.querySelector('.button-right-Blockbusters');
    var left_button_block= document.querySelector('.button-left-Blockbusters');
    var track_Blockbusters= document.querySelector('.blockbusters__track');
    // var amount_to_move_block= document.querySelector('.first-block').getBoundingClientRect().width;
    // console.log(amount_to_move_block);
    
    j=0;
    var move_to_the_right_Blockbusters= (track_Blockbusters)=> {
        for(j=j; j<=1; j++){
            if(j>1)
                return;
            else
                j++;
            track_Blockbusters.style.transform= 'translateX(-' + (amount_to_move+99)*j+ 'px)';
            amount_aleady_moved_block= (amount_to_move+99)*j;
            return;
        }
    }

    var move_to_the_left_Blockbusters= (track_Blockbusters)=> {
        for(j=j; j>0; j--){
            if(j<1)
                return;
            else
                j--;
            track_Blockbusters.style.transform= 'translateX(-' + (amount_to_move+99)*j+ 'px)';
            amount_aleady_moved_block= (amount_to_move+99)*j;    
            return;
            
        }
    }

    
    var hide_button_blockbusters= (right_button_block, left_button_block, amount_aleady_moved_block)=>{
        if(amount_aleady_moved_block=== (amount_to_move+99)*2){
            right_button_block.classList.add('be-hidden');
            left_button_block.classList.remove('be-hidden');
        }
        else if(amount_aleady_moved_block===0){
            right_button_block.classList.remove('be-hidden');
            left_button_block.classList.add('be-hidden');
        }
        else{
            right_button_block.classList.remove('be-hidden');
            left_button_block.classList.remove('be-hidden');
        }
    }

    right_button_block.addEventListener('click', e=>{
        move_to_the_right_Blockbusters(track_Blockbusters);
        hide_button_blockbusters(right_button_block, left_button_block, amount_aleady_moved_block);
        console.log(amount_aleady_moved_block);
    });
   
    left_button_block.addEventListener('click', e=>{
        move_to_the_left_Blockbusters(track_Blockbusters);
        hide_button_blockbusters(right_button_block, left_button_block, amount_aleady_moved_block);
        console.log(amount_aleady_moved_block);
    });

    
    var visible_more= document.querySelector('.more');


    visible_more.addEventListener('click', e=>{
        
    })
  

}

