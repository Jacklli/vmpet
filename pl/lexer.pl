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

our @tokens = ();
sub lex() {
    (our $characters, @token_exprs) = @_;
    $pos = 0;
    $textlen = length($characters);
    $n = @token_exprs;
    while($pos < $textlen) {
        for($i = 0; $i < $n; $i++) {
            ($pattern,$tag) = ($token_exprs[$i][0], $token_exprs[$i][1]);
            $characters =~ /($pattern)/;
            if(defined($1) && $1 ne '') {
               $tmplen = length($1);
               $tmpchr = substr($characters,0,$tmplen);
               if($tmpchr eq $1 and $tag ne 'None') {
                   @token = ($1,$tag);
                   if($pattern eq '\*') {
                       $tmpchr = '\\'.$tmpchr;  # we need to \ it when it's special characters like '*'
                   }
                   $characters =~ s/$tmpchr//;
                   $pos += $tmplen;
                   push @tokens,[@token];
#                   print "pos is $pos\n";
                   break;
               } elsif($tmpchr eq $1 and $tag eq 'None') {
                   $characters =~ s/$tmpchr//;
                   $pos += $tmplen;
#                   print "pos is $pos\n";
               }
            }
        }
    }
}

&lex("n := 5;
p := 1;
while n > 0 do
  p := p * n;
  n := n - 1
end
",@token_exprs);

$n = @tokens;
for($i=0;$i<$n;$i++) {
    print "\$tokens[$i][0] is $tokens[$i][0]\n";
}
