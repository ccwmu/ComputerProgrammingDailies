import pygame, sys, random, time

W, H = 800, 600
ROWS, COLS = 5, 11
ALIEN_W, ALIEN_H = 40, 30
PLAYER_W, PLAYER_H = 60, 18
BULLET_W, BULLET_H = 4, 12

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_W, PLAYER_H))
        self.image.fill((0, 255, 120))
        self.rect = self.image.get_rect(midbottom=(W//2, H-30))
        self.speed = 6
        self.cooldown = 250
        self.last_shot = 0
        self.invuln_until = 0
    def update(self, keys):
        dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.rect.x += dx * self.speed
        if self.rect.left < 10: self.rect.left = 10
        if self.rect.right > W-10: self.rect.right = W-10
    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot >= self.cooldown
    def shoot(self, group, all_sprites):
        if self.can_shoot():
            b = Bullet(self.rect.midtop, -10, (255, 255, 255))
            group.add(b); all_sprites.add(b)
            self.last_shot = pygame.time.get_ticks()
    def hit(self):
        self.invuln_until = pygame.time.get_ticks() + 2000
    def invulnerable(self):
        return pygame.time.get_ticks() < self.invuln_until

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vy, color):
        super().__init__()
        self.image = pygame.Surface((BULLET_W, BULLET_H))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.vy = vy
    def update(self, keys=None):
        self.rect.y += self.vy
        if self.rect.bottom < 0 or self.rect.top > H: self.kill()

class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y, col, row):
        super().__init__()
        self.image = pygame.Surface((ALIEN_W, ALIEN_H))
        colors = [(80,200,120),(120,200,255),(255,180,80),(255,120,160),(200,160,255)]
        self.image.fill(colors[row % len(colors)])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.col = col
        self.row = row

def spawn_aliens(level, aliens, all_sprites):
    aliens.empty()
    ox, oy = 80, 80
    gapx, gapy = 20, 20
    for r in range(ROWS):
        for c in range(COLS):
            x = ox + c*(ALIEN_W+gapx)
            y = oy + r*(ALIEN_H+gapy)
            a = Alien(x, y, c, r)
            aliens.add(a); all_sprites.add(a)
    speed = 1.0 + 0.12*level
    return speed

def bottom_shooters(aliens):
    per_col = {}
    for a in aliens:
        if a.col not in per_col or a.rect.bottom > per_col[a.col].rect.bottom:
            per_col[a.col] = a
    return list(per_col.values())

def draw_text(surf, txt, size, pos, color=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    img = font.render(txt, True, color)
    rect = img.get_rect(topleft=pos)
    surf.blit(img, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group(player)
    aliens = pygame.sprite.Group()
    player_bullets = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()

    level = 1
    score = 0
    lives = 3
    dx = spawn_aliens(level, aliens, all_sprites)
    direction = 1
    move_down = False

    ALIEN_FIRE = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_FIRE, 700)

    running = True
    game_over = False

    while running:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.shoot(player_bullets, all_sprites)
                if event.type == ALIEN_FIRE and aliens:
                    shooters = bottom_shooters(aliens)
                    shooter = random.choice(shooters)
                    b = Bullet(shooter.rect.midbottom, 6+level, (255, 80, 80))
                    alien_bullets.add(b); all_sprites.add(b)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        level = 1
                        score = 0
                        lives = 3
                        player.rect.midbottom = (W//2, H-30)
                        player.invuln_until = 0
                        for g in (aliens, player_bullets, alien_bullets): g.empty()
                        all_sprites.empty(); all_sprites.add(player)
                        dx = spawn_aliens(level, aliens, all_sprites)
                        direction = 1
                        move_down = False
                        game_over = False
                    if event.key == pygame.K_ESCAPE:
                        running = False

        keys = pygame.key.get_pressed()
        if not game_over:
            player.update(keys)
            player_bullets.update()
            alien_bullets.update()

            if aliens:
                min_x = min(a.rect.left for a in aliens)
                max_x = max(a.rect.right for a in aliens)
                edge_hit = (max_x >= W-10 and direction > 0) or (min_x <= 10 and direction < 0)
                if edge_hit:
                    direction *= -1
                    move_down = True
                    dx *= 1.05
                for a in aliens:
                    a.rect.x += int(direction * dx)
                if move_down:
                    for a in aliens:
                        a.rect.y += 16
                    move_down = False

            hits = pygame.sprite.groupcollide(aliens, player_bullets, True, True)
            if hits:
                score += sum(10*(1 + v.row) for v in hits.keys())

            if not player.invulnerable():
                if pygame.sprite.spritecollide(player, alien_bullets, True):
                    lives -= 1
                    player.hit()
                    player.rect.midbottom = (W//2, H-30)
                if pygame.sprite.spritecollide(player, aliens, False):
                    lives -= 1
                    player.hit()
                    player.rect.midbottom = (W//2, H-30)

            if aliens and max(a.rect.bottom for a in aliens) >= H-60:
                if not player.invulnerable():
                    lives -= 1
                    player.hit()
                    player.rect.midbottom = (W//2, H-30)

            if lives <= 0:
                game_over = True

            if not aliens:
                level += 1
                dx = spawn_aliens(level, aliens, all_sprites)
                direction = 1

        screen.fill((10, 10, 20))
        for s in all_sprites:
            if s is player and player.invulnerable() and (pygame.time.get_ticks()//120) % 2 == 0:
                pass
            else:
                screen.blit(s.image, s.rect)

        draw_text(screen, f"Score: {score}", 28, (10, 8))
        draw_text(screen, f"Lives: {lives}", 28, (W-150, 8))
        draw_text(screen, f"Level: {level}", 28, (W//2-50, 8))

        if game_over:
            draw_text(screen, "GAME OVER", 72, (W//2-190, H//2-60), (255,80,80))
            draw_text(screen, "Press R to Restart or Esc to Quit", 28, (W//2-200, H//2+10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()