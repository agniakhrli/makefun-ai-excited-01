// ai-excited-01 submission entrypoint (Node 22, standard library only)
// Copies entry.png to the grading output directory (MAKEFUN_OUTPUT_DIR or /output).
import { copyFileSync, mkdirSync } from 'node:fs';
import { resolve, join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });

const sourcePath = resolve(import.meta.url.replace(/^file:\/\//, ''), '../entry.png');
// On Windows / URL normalization fallback
const src = new URL('./entry.png', import.meta.url);
const dest = join(outputDir, 'entry.png');

copyFileSync(src, dest);
