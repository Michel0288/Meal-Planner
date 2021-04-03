/* Add your Application JavaScript */
onload=function(){ 

    button = document.getElementById('IngredientsButton')
    
    function AddField(){
        button.innerHTMT +=  "{{ form.ingredient_name(class='form-control') }}"

    }

}