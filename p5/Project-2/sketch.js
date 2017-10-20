function setup() {
  createCanvas(1000,800);
  background(60,10,0);
}

function draw() {
  for (let x = 10; x < 300; x += 10){
  fill(x + 30, x + 5, x + 10);
  rect(x, x, x, 300);}
  owl(440,490);}
  function owl(x,y){
    push();
    translate(x,y);
    stroke(204,102,0);
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
    fill(204,102,0);
    noStroke(0);
    //
      fill(random(250),random(100),random(0));
    quad(28,-28,32,-21,28,-14,24,-21)
      fill(random(250),random(100),random(0));
    quad(28,-35,32,-28,28,-21,24,-28);
      fill(random(250),random(100),random(0));
    quad(28,-42,32,-35,28,-28,24,-35);
    //
      fill(random(250),random(100),random(0));
    quad(21,-22,25,-15,21,-8,17,-15)
      fill(random(250),random(100),random(0));
    quad(21,-29,25,-22,21,-15,17,-22);
      fill(random(250),random(100),random(0));
    quad(21,-36,25,-29,21,-22,17,-29);
    //
      fill(random(250),random(100),random(0));
    quad(14,-18,18,-11,14,-4,10,-11)
      fill(random(250),random(100),random(0));
    quad(14,-25,18,-18,14,-11,10,-18);
      fill(random(250),random(100),random(0));
    quad(14,-32,18,-25,14,-18,10,-25);
    //
      fill(random(250),random(100),random(0));
    quad(7,-16,11,-9,7,-2,3,-9)
      fill(random(250),random(100),random(0));
    quad(7,-23,11,-16,7,-9,3,-16);
      fill(random(250),random(100),random(0));
    quad(7,-30,11,-23,7,-16,3,-23);
    //middle
      fill(random(250),random(100),random(0));
    quad(0,-16,4,-9,0,-2,-4,-9);
      fill(random(250),random(100),random(0));
    quad(0,-23,4,-16,0,-9,-4,-16);
      fill(random(250),random(100),random(0));
    quad(0,-30,4,-23,0,-16,-4,-23)
    //
      fill(random(250),random(100),random(0));
    quad(-7,-16,-3,-9,-7,-2,-11,-9)
      fill(random(250),random(100),random(0));
    quad(-7,-23,-3,-16,-7,-9,-11,-16);
      fill(random(250),random(100),random(0));
    quad(-7,-30,-3,-23,-7,-16,-11,-23);
    //
      fill(random(250),random(100),random(0));
    quad(-14,-18,-10,-11,-14,-4,-18,-11)
      fill(random(250),random(100),random(0));
    quad(-14,-25,-10,-18,-14,-11,-18,-18);
      fill(random(250),random(100),random(0));
    quad(-14,-32,-10,-25,-14,-18,-18,-25);
    //
      fill(random(250),random(100),random(0));
    quad(-21,-22,-17,-15,-21,-8,-25,-15)
      fill(random(250),random(100),random(0));
    quad(-21,-29,-17,-22,-21,-15,-25,-22);
      fill(random(250),random(100),random(0));
    quad(-21,-36,-17,-29,-21,-22,-25,-29);
    //
      fill(random(250),random(100),random(0));
    quad(-28,-28,-24,-21,-28,-14,-32,-21)
      fill(random(250),random(100),random(0));
    quad(-28,-35,-24,-28,-28,-21,-32,-28);
      fill(random(250),random(100),random(0));
    quad(-28,-42,-24,-35,-28,-28,-32,-35);
    pop();
  }


