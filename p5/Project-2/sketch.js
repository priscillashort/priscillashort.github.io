function setup() {
  createCanvas(1000,800);
  //createImage(leaves.jpg);
  //centerCanvas();
  background(60,10,0);
}

function draw() {
  ellipse(100,100,80,80);
  ellipse(100,200,80,80);
  for (let x = 10; x < 200; x += 10){
    fill(x + 30, x + 5, x + 10);
    rect(x, x + 5, x * 5, 200);
  }
  translate(110,110);
  stroke(0);
  strokeWeight(70);
  line(0,-35,0,-65);
  noStroke();
  fill(204);
  ellipse(-17.5,-65,35,35);
  ellipse(17.5,-65,35,35);
  arc(0,-65,70,70,0,PI);
  fill(0);
  ellipse(-14,-65,8,8);
  ellipse(14,-65,8,8);
  quad(0,-58,4,-51,0,-44,-4,-51);
  fill(255);
  quad(0,-30,4,-23,0,-16,-4,-23);
  //quad(0,-58,4,-51,0,-44,-4,-51);
  //quad(0,-58,4,-51,0,-44,-4,-51);
  //quad(0,-58,4,-51,0,-44,-4,-51);
  //quad(0,-58,4,-51,0,-44,-4,-51);
  //if(mouseIsPressed){
  //  fill(0);
 // } else {
 //   fill(random(170),random(20),random(0));
 // }
  //ellipse(mouseX,mouseY,40,40);
 // rect(mouseX,mouseY,40,40);
}


