(define (problem DLOG-5-7-10)
	(:domain driverlog)
	(:objects
	driver1 - driver
	driver2 - driver
	driver3 - driver
	driver4 - driver
	driver5 - driver
	truck1 - truck
	truck2 - truck
	truck3 - truck
	truck4 - truck
	truck5 - truck
	truck6 - truck
	truck7 - truck
	package1 - obj
	package2 - obj
	package3 - obj
	package4 - obj
	package5 - obj
	package6 - obj
	package7 - obj
	package8 - obj
	package9 - obj
	package10 - obj
	s0 - location
	s1 - location
	s2 - location
	s3 - location
	s4 - location
	s5 - location
	p0-1 - location
	p0-2 - location
	p0-5 - location
	p1-0 - location
	p1-3 - location
	p2-0 - location
	p2-5 - location
	p3-4 - location
	p3-5 - location
	p5-4 - location
	)
	(:init
	(at driver1 s0)
	(at driver2 s4)
	(at driver3 s3)
	(at driver4 s4)
	(at driver5 s1)
	(at truck1 s5)
	(empty truck1)
	(at truck2 s1)
	(empty truck2)
	(at truck3 s1)
	(empty truck3)
	(at truck4 s2)
	(empty truck4)
	(at truck5 s4)
	(empty truck5)
	(at truck6 s5)
	(empty truck6)
	(at truck7 s1)
	(empty truck7)
	(at package1 s3)
	(at package2 s2)
	(at package3 s5)
	(at package4 s0)
	(at package5 s2)
	(at package6 s4)
	(at package7 s1)
	(at package8 s4)
	(at package9 s4)
	(at package10 s3)
	(path s0 p0-1)
	(path p0-1 s0)
	(path s1 p0-1)
	(path p0-1 s1)
	(path s0 p0-2)
	(path p0-2 s0)
	(path s2 p0-2)
	(path p0-2 s2)
	(path s0 p0-5)
	(path p0-5 s0)
	(path s5 p0-5)
	(path p0-5 s5)
	(path s1 p1-3)
	(path p1-3 s1)
	(path s3 p1-3)
	(path p1-3 s3)
	(path s2 p2-5)
	(path p2-5 s2)
	(path s5 p2-5)
	(path p2-5 s5)
	(path s3 p3-4)
	(path p3-4 s3)
	(path s4 p3-4)
	(path p3-4 s4)
	(path s3 p3-5)
	(path p3-5 s3)
	(path s5 p3-5)
	(path p3-5 s5)
	(path s5 p5-4)
	(path p5-4 s5)
	(path s4 p5-4)
	(path p5-4 s4)
	(link s0 s2)
	(link s2 s0)
	(link s0 s4)
	(link s4 s0)
	(link s1 s5)
	(link s5 s1)
	(link s2 s1)
	(link s1 s2)
	(link s2 s3)
	(link s3 s2)
	(link s2 s4)
	(link s4 s2)
	(link s2 s5)
	(link s5 s2)
	(link s3 s0)
	(link s0 s3)
	(link s3 s1)
	(link s1 s3)
	(link s3 s4)
	(link s4 s3)
	(link s3 s5)
	(link s5 s3)
	(link s4 s1)
	(link s1 s4)
	(link s5 s4)
	(link s4 s5)
)
	(:goal (and
	(at driver1 s5)
	(at driver3 s0)
	(at driver4 s0)
	(at truck2 s0)
	(at truck3 s2)
	(at truck4 s5)
	(at truck5 s1)
	(at truck6 s1)
	(at truck7 s0)
	(at package1 s3)
	(at package2 s2)
	(at package3 s3)
	(at package4 s3)
	(at package5 s5)
	(at package6 s0)
	(at package7 s3)
	(at package8 s2)
	(at package9 s1)
	(at package10 s3)
	))


)
