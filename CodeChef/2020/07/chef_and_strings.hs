module Main where
import Control.Monad
import Data.List


getInt = readLn :: IO Int


getInts :: IO [Int]
getInts = map read . words <$> getLine


main :: IO ()
main = do
  t <- getInt
  replicateM_ t $ do
    _ <- getInt
    ps <- getInts
    let ps' = tail ps
        diff = [abs(abs(x-y) - 1) | (x, y) <- zip ps ps']
    print $ sum diff
