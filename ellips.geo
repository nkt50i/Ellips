SetFactory("OpenCASCADE");
lc = 0.05;

H = 1; L = 1;
r1 = 0.225; r2 = 0.125;
x_c = 0.5; y_c = 0.5;

Point(1) = {0, 0, 0, lc};
Point(2) = {L, 0, 0, lc};
Point(3) = {L, H, 0, lc};
Point(4) = {0, H, 0, lc};
Point(5) = {x_c, y_c, 0, lc};

Line(6) = {1, 2};
Line(7) = {2, 3};
Line(8) = {3, 4};
Line(9) = {4, 1};

Curve Loop(10) = {6, 7, 8, 9};
Surface(16) = {10};

// Создание эллиптических дуг
Ellipse(11) = {x_c, y_c, 0, r1, r2, 0, Pi/2};
Ellipse(12) = {x_c, y_c, 0, r1, r2, Pi/2, Pi};
Ellipse(13) = {x_c, y_c, 0, r1, r2, -Pi, -Pi/2};
Ellipse(14) = {x_c, y_c, 0, r1, r2, -Pi/2, 0};

// Поворот эллиптических дуг перед созданием поверхности
Rotate {{0, 0, 1}, {x_c, y_c, 0}, Pi/4} { Curve{11, 12, 13, 14}; }

Curve Loop(15) = {11, 12, 13, 14};
Surface(17) = {15};

// Удаляем только ненужные точки, НЕ удаляем кривые!
Delete {  Point {15}; Point {18}; }

BooleanDifference(20) = { Surface{16}; Delete; } { Surface{17}; Delete; };

// Сгущение сетки к эллипсу
Field[1] = Attractor;
Field[1].NodesList = {5}; 
Field[2] = Threshold;
Field[2].IField = 1;
Field[2].LcMin = lc / 10;
Field[2].LcMax = lc;
Field[2].DistMin = r1 / 2;
Field[2].DistMax = r1 * 2;
Background Field = 2;

Coherence;
Mesh 2;
