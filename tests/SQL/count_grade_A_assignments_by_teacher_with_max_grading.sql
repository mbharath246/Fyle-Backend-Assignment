-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH graded_counts AS (
    SELECT teacher_id, COUNT(*) AS num_graded
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
)
SELECT COUNT(*) AS grade_a_count
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM graded_counts
    WHERE num_graded = (SELECT MAX(num_graded) FROM graded_counts)
)
AND grade = 'A';
