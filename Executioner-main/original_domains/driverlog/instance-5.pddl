(define (problem DLOG-8-10-15)
	(:domain driverlog)
	(:objects
	driver1 - driver
	driver2 - driver
	driver3 - driver
	driver4 - driver
	driver5 - driver
	driver6 - driver
	driver7 - driver
	driver8 - driver
	truck1 - truck
	truck2 - truck
	truck3 - truck
	truck4 - truck
	truck5 - truck
	truck6 - truck
	truck7 - truck
	truck8 - truck
	truck9 - truck
	truck10 - truck
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
	package11 - obj
	package12 - obj
	package13 - obj
	package14 - obj
	package15 - obj
	s0 - location
	s1 - location
	s2 - location
	s3 - location
	s4 - location
	s5 - location
	s6 - location
	s7 - location
	p0-1 - location
	p0-2 - location
	p0-7 - location
	p1-0 - location
	p1-2 - location
	p1-3 - location
	p2-0 - location
	p2-6 - location
	p3-1 - location
	p3-4 - location
	p4-5 - location
	p4-7 - location
	)
	(:init
	(at driver1 s3)
	(at driver2 s5)
	(at driver3 s7)
	(at driver4 s2)
	(at driver5 s4)
	(at driver6 s3)
	(at driver7 s6)
	(at driver8 s0)
	(at truck1 s2)
	(empty truck1)
	(at truck2 s6)
	(empty truck2)
	(at truck3 s2)
	(empty truck3)
	(at truck4 s6)
	(empty truck4)
	(at truck5 s6)
	(empty truck5)
	(at truck6 s5)
	(empty truck6)
	(at truck7 s1)
	(empty truck7)
	(at truck8 s7)
	(empty truck8)
	(at truck9 s6)
	(empty truck9)
	(at truck10 s7)
	(empty truck10)
	(at package1 s1)
	(at package2 s5)
	(at package3 s3)
	(at package4 s1)
	(at package5 s1)
	(at package6 s3)
	(at package7 s6)
	(at package8 s6)
	(at package9 s1)
	(at package10 s1)
	(at package11 s5)
	(at package12 s1)
	(at package13 s6)
	(at package14 s0)
	(at package15 s4)
	(path s0 p0-1)
	(path p0-1 s0)
	(path s1 p0-1)
	(path p0-1 s1)
	(path s0 p0-2)
	(path p0-2 s0)
	(path s2 p0-2)
	(path p0-2 s2)
	(path s0 p0-7)
	(path p0-7 s0)
	(path s7 p0-7)
	(path p0-7 s7)
	(path s1 p1-2)
	(path p1-2 s1)
	(path s2 p1-2)
	(path p1-2 s2)
	(path s1 p1-3)
	(path p1-3 s1)
	(path s3 p1-3)
	(path p1-3 s3)
	(path s2 p2-6)
	(path p2-6 s2)
	(path s6 p2-6)
	(path p2-6 s6)
	(path s3 p3-4)
	(path p3-4 s3)
	(path s4 p3-4)
	(path p3-4 s4)
	(path s4 p4-5)
	(path p4-5 s4)
	(path s5 p4-5)
	(path p4-5 s5)
	(path s4 p4-7)
	(path p4-7 s4)
	(path s7 p4-7)
	(path p4-7 s7)
	(link s0 s6)
	(link s6 s0)
	(link s1 s2)
	(link s2 s1)
	(link s1 s6)
	(link s6 s1)
	(link s2 s7)
	(link s7 s2)
	(link s3 s1)
	(link s1 s3)
	(link s3 s2)
	(link s2 s3)
	(link s3 s4)
	(link s4 s3)
	(link s3 s5)
	(link s5 s3)
	(link s3 s6)
	(link s6 s3)
	(link s4 s1)
	(link s1 s4)
	(link s4 s6)
	(link s6 s4)
	(link s5 s0)
	(link s0 s5)
	(link s5 s1)
	(link s1 s5)
	(link s5 s2)
	(link s2 s5)
	(link s7 s1)
	(link s1 s7)
	(link s7 s6)
	(link s6 s7)
)
	(:goal (and
	(at driver1 s7)
	(at driver2 s1)
	(at driver3 s2)
	(at driver4 s0)
	(at driver5 s4)
	(at driver6 s3)
	(at truck1 s7)
	(at truck2 s0)
	(at truck3 s4)
	(at truck4 s2)
	(at truck6 s4)
	(at truck7 s0)
	(at truck8 s4)
	(at truck9 s3)
	(at truck10 s3)
	(at package1 s6)
	(at package2 s5)
	(at package3 s7)
	(at package4 s5)
	(at package5 s3)
	(at package6 s1)
	(at package7 s2)
	(at package8 s2)
	(at package9 s0)
	(at package10 s0)
	(at package11 s2)
	(at package12 s7)
	(at package13 s2)
	(at package14 s4)
	(at package15 s5)
	))


)
