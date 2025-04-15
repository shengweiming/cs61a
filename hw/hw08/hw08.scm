(define (ascending? s) 
(if (<= (length s) 1)
    #t
    (and (<= (car s) (car (cdr s)))   (ascending? (cdr s)))
))



(define (my-filter pred s) 
(if (null? s)
    s
    (if (pred (car s))
        (append (list (car s)) (my-filter pred (cdr s)))
        (my-filter pred (cdr s))    )
))



(define (interleave lst1 lst2)
(cond 
((null? lst1)
    lst2)
((null? lst2)
    lst1)
(else
    (append (list (car lst1)) 
            (list (car lst2))
            (interleave (cdr lst1) (cdr lst2)))
)))



(define (no-repeats s) 
(if (<= (length s) 1)
    s

    (let ((a (car s)))
    
    (append (list a)
            (no-repeats (filter (lambda (x) (not (= x a)))
                                 (cdr s)))
                                 
    )
    
    )
    

)

)


(filter (lambda (x) (not (= x 1)) )'(1 2 3 4))