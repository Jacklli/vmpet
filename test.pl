our $line = "n := *;";
our $line1 = "";
$line =~ s/([a-z])//o;
$line1 = $line;
print "$line \n";
$line = $line;
$pattern = '\\'.'*';
$line1 =~ s/($pattern)//;
print "$line1 \n";
