calculate :: Double ->String->Double->IO()
calculate n1 opr n2 = do
    if opr == "+"
    then print(n1 + n2)
    else if opr == "-"
    then print(n1 - n2)
    else if opr == "*"
    then print(n1 * n2)
    else if opr == "/"
    then print(n1 / n2)
    else putStrLn "Invalid"
    
main :: IO ()
main =  do
    putStrLn "Enter n1"
    strN1 <- getLine
    putStrLn "Enter operator"
    opr <- getLine
    putStrLn "Enter n2"
    strN2 <- getLine
    let n1 = read strN1::Double
    let n2 = read strN2::Double
    calculate n1 opr n2
