function setup() {
  createCanvas(800,600);
  //angleMode(DEGREES);
}

function draw() {
  //background(204);
  strokeWeight(8);
  arc(90,460,80,80,0,HALF_PI);
  arc(190,460,80,80,0,PI+HALF_PI);
  arc(290,460,80,80,PI,TWO_PI+HALF_PI);
  arc(390,460,80,80,QUARTER_PI,PI+QUARTER_PI);
  arc(490,460,80,80,0,radians(270));
  strokeWeight(1);
  //noFill();
  //noStroke();
  fill(0,255,0);
  ellipse(278,-100,400,400);
  fill(0,0,255);
  ellipse(120,100,110,110);
  fill(0,0,255,160);
  ellipse(140,80,110,110);
  fill(255,0,0);
  ellipse(412,60,18,18);
  fill(255);
  strokeWeight(5);
  strokeJoin(ROUND);
  quad(458,55,499,14,692,66,651,107);
  triangle(647,54,692,9,692,66);
  triangle(458,55,590,91,590,112);
  strokeWeight(7);
  strokeJoin(BEVEL);
  fill(101);
  rect(180,250,220,40);
  fill(255);
  strokeWeight(4);
  strokeCap(SQUARE); //or ROUND
  line(20,150,420,210)
  strokeWeight(1);
  point(400,300);
  point(401,300);
  point(402,300);
  point(403,300);
  point(0,0);
  point(799,599);
  point(799,0);
  point(0,599);
  if(mouseIsPressed){
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX,mouseY,40,40);
}


