
    (define (problem instance-1)
    (:domain  blocksworld-4ops)
    (:objects
        
	b4
	b5
	b1
	b2
	b3)
(:init	(on b1 b2)
	(on b3 b4)
	(arm-empty )
	(clear b3)
	(clear b1)
	(clear b5)
	(injected-0 )
	(on-table b4)
	(on-table b2)
	(on-table b5))(:goal
        (and (on b1 b3) (on b2 b5) (on b3 b2) (on b5 b4) (injected-0 ))
        )
    )
    