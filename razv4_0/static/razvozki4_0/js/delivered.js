function closeDeliveredRazvozka(obj){
    document.querySelector('#rzv_id').value = obj.dataset.id;
    document.querySelector('#returnOtherModal').style.display = 'block';
}

function closeDeliveredModal(){
    document.querySelector('#return_close_without_delivery').value = null;
    document.querySelector('#returnOtherModal').style.display = 'none';
}