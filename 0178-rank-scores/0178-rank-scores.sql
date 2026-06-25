# Write your MySQL query statement below
select score,Dense_Rank() Over(Order By score Desc) As "rank" from scores order by Score DESC