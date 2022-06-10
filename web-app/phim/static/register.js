function alreadyloaded(){
    $(document).ready(function(){
        $('.input-eye').click(function(){
            $(this).toggleClass('reveal');
            $(this).children('i').toggleClass('fa-eye fa-eye-slash');
            if($(this).hasClass('reveal'))
                $(this).prev('input').attr('type', 'text');
            else
                $(this).prev('input').attr('type', 'password');
        });
    })
}