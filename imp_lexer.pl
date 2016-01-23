# vmpet is an interpreter writen by Liyinlong which is
# developend for research.
# it is released in GPL v2 License.
# All rights reserved. Liyinlong (yinlong.lee at hotmail.com)

$RESERVED = 'RESERVED';
$INT      = 'INT';
$ID       = 'ID';

@token_exprs = ( 
    ['[ \n\t]+',             'None'],
    ['#[^\n]*',              'None'],
    ['\:=',                  $RESERVED],
    ['\[',                   $RESERVED],
    ['\]',                   $RESERVED],
    [';',                    $RESERVED],
    ['\+',                   $RESERVED],
    ['-',                    $RESERVED],
    ['\*',                   $RESERVED],
    ['/',                    $RESERVED],
    ['<=',                   $RESERVED],
    ['<',                    $RESERVED],
    ['>=',                   $RESERVED],
    ['>',                    $RESERVED],
    ['!=',                   $RESERVED],
    ['=',                    $RESERVED],
    ['and',                  $RESERVED],
    ['or',                   $RESERVED],
    ['not',                  $RESERVED],
    ['if',                   $RESERVED],
    ['then',                 $RESERVED],
    ['else',                 $RESERVED],
    ['while',                $RESERVED],
    ['do',                   $RESERVED],
    ['end',                  $RESERVED],
    ['[0-9]+',               $INT],
    ['[A-Za-z][A-Za-z0-9_]*',$ID]
);
