/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function(A) {
    var res = A.map(function(row) {
        var revrow = row.reverse();
        return revrow.map(x=>1-x);
    });
    return res;
};