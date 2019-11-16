
AREA_W = 1200;
AREA_H = 600;

var img_meeting_table = new Image();
img_meeting_table.src = 'static/img/meeting_table.png';

function _draw_borders(ctx){
    ctx.rect(0, 0, AREA_W, AREA_H);
}

function _draw_person(ctx, person){
    ctx.strokeStyle = 'rgba(0, 0, 0, 1)';
    ctx.fillStyle = 'rgba(50, 150, 255, 1)';
    ctx.fillRect(person.x, person.y, 15, 15);    
}

function _draw_room(ctx, room){
    ctx.clearRect(room.x, room.y, room.x_size, room.y_size);
    ctx.strokeStyle = 'rgba(0, 0, 0, 1)';
    ctx.rect(room.x, room.y, room.x_size, room.y_size);
    ctx.fillStyle = 'rgba(192,192,192, 1.0)';
    ctx.fillRect(room.x, room.y, room.x_size, room.y_size);
    ctx.fillStyle = room.lamp;
    ctx.fillRect(room.x, room.y, room.x_size, room.y_size);
    ctx.font = "20px Arial";
    ctx.fillStyle = 'rgba(0, 0, 0, 1)';
    ctx.fillText(room.name, room.x+20, room.y+30);
    ctx.font = "14px Arial";
    ctx.fillStyle = 'rgba(0, 0, 0, 1)';
    ctx.fillText(room.lamp_power_str, room.x+20, room.y+60);
    ctx.fillText(room.room_temp_str, room.x+20, room.y+80);
}

function _draw_images(ctx){
    ctx.globalAlpha = 0.8;
    ctx.drawImage(img_meeting_table, 800, 230);
    ctx.globalAlpha = 1.0;
}

function draw_state(state){
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    // Rooms
    for(var i=0; i<state.rooms.length; i++){
        var room = state.rooms[i];
        _draw_room(ctx, room);
    }
    // Add images
    _draw_images(ctx);
    // Persons
    for(var i=0; i<state.persons.length; i++){
        var person = state.persons[i];
        _draw_person(ctx, person);
    }
    // End
    ctx.stroke();
}

function update_user(x, y){
    
    var user_action = $('input[name=user_action]:checked').val();
    var api_uri = '/update/user?x='+x+'&y='+y+'&a='+user_action;

    $.ajax({
        url: api_uri,
        dataType: 'json',
        async: true,
        success: function(resp) {
        }
    });
}

function async_animation(){
    var api_uri = '/run/json';
    $.ajax({
        url: api_uri,
        dataType: 'json',
        async: true,
        success: function(resp) {
            var state = resp.state_data;
            draw_state(state);
        }
    });
}
