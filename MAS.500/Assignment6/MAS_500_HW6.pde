// MAS.500 Homework 6
//
// Drag mouse to change the color of the circle
// depending on position.

void setup() {
  size(500, 500);
}

void draw() {
  background(255);
  noStroke();
  float x = (float) mouseX/width;
  float y = (float) mouseY/height;
  println(x); println(y);
  color interpColor = color(int(x * 255), int(y * 255), int((1 - x) * 255));
  fill(interpColor);
  ellipse(mouseX, mouseY, 50, 50);
  noFill();
}
