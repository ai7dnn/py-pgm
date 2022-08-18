# 방법1
print(" Subject : Python Language\n\n Name    : %s \n" \
      " Major   : %s \n\n Total  Average  Grade  Rank \n" \
      "  %3d    %5.1f     %1c     %2d"  \
      % (name, major, total, avg, grade, ranking))

# 방법2
print(" Subject : Python Language\n")
print(" Name    : %s" % name)
print(" Major   : %s\n" % major)
print(" Total  Average  Grade  Rank")
print("  %3d    %5.1f     %1c     %2d"    % (total, avg, grade, ranking))
