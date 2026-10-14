# Daily questions

The heartbeat of Epilogue Life: two or three questions a morning, answered by message,
saved as they are answered.

## Prompt (give this to your assistant)

Install this as a daily cron job at my preferred time, delivering to this chat:

> Morning. Run `scripts/next_questions.py` for my plan folder, then ask me the returned
> questions one at a time in your warm Epilogue Life voice. Save each answer to the right
> file in shared/answers/ and update progress.json. Two or three questions only; if I say
> skip, record skipped and move on. If I do not reply today, no follow-up; we try again
> tomorrow.

## Notes

- Preferred time lives in shared/profile.md ("How I like to work").
- The script returns unanswered questions first, then deferred ones, never skipped ones.
- If every question is answered or skipped, the run says so once and goes quiet forever
  (the monthly review remains).
