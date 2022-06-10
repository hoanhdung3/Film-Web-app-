function alreadyloaded(){
    var track= document.querySelector('.track');
    var slides= Array.from(track.children);
    var slide_width= slides[0].getBoundingClientRect().width;
    var right_button= document.querySelector('.right-button');
    var left_button=document.querySelector('.left-button');
    console.log(slide_width);

    var set_slides= (slides)=>{
        for(i=0; i<slides.length; i++)
        {
            slides[i].style.left= slide_width*i+ 1 + 21*i + 'px';
        }


    }

    set_slides(slides);

    right_button.addEventListener('click', e=>{
        track.style.transform= 'translateX(-'+ ((slide_width+ 1 + 21)*6 - 10) +'px)';
    });

    left_button.addEventListener('click', e=>{
        track.style.transform= 'translateX('+ 0 +'px)';
    });
}