rm _build -Rf;
mkdir _build;
cd Slides;
landslide slides.cfg
firefox ../_build/slides.html;
cd -;
