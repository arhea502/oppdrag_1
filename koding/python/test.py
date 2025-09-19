import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1500, 900
PLAYER_SIZE = 50
ZOMBIE_SIZE = 50
BULLET_SIZE = 5
FPS = 60
INITIAL_FIRE_RATE = 1000  # milliseconds
FIRE_RATE_DECREASE = 100  # milliseconds decrease per upgrade
MONEY_PER_KILL = 10  # Amount of money earned per kill
HEALTH_COST = 20  # Cost to purchase health
FIRE_RATE_UPGRADE_COST = 50  # Cost to upgrade fire rate
AIMBOT_COST = 200  # Cost to purchase aimbot
ZOMBIES_PER_WAVE = 5  # Number of zombies to spawn per wave
WAVE_DURATION = 300  # Duration of each wave (in seconds)
EXPLOSIVE_TOGGLE_DELAY = 2000  # 2 seconds in milliseconds

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
        self.hp = 100
        self.money = 0
        self.aimbot_enabled = False
        self.fire_rate_level = 0  # Number of fire rate upgrades

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def purchase_health(self):
        if self.money >= HEALTH_COST:
            self.hp += 20
            self.money -= HEALTH_COST

    def upgrade_fire_rate(self):
        global FIRE_RATE_UPGRADE_COST
        if self.money >= FIRE_RATE_UPGRADE_COST:
            self.fire_rate_level += 1
            self.money -= FIRE_RATE_UPGRADE_COST
            FIRE_RATE_UPGRADE_COST += 10  # Increase cost for next upgrade

    def get_fire_rate(self):
        return max(100, INITIAL_FIRE_RATE - self.fire_rate_level * FIRE_RATE_DECREASE)

    def purchase_aimbot(self):
        if self.money >= AIMBOT_COST:
            self.aimbot_enabled = True
            self.money -= AIMBOT_COST

# Zombie class
class Zombie:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ZOMBIE_SIZE), random.randint(0, HEIGHT - ZOMBIE_SIZE), ZOMBIE_SIZE, ZOMBIE_SIZE)

    def move_towards_player(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += 1
        elif self.rect.x > player.rect.x:
            self.rect.x -= 1
        if self.rect.y < player.rect.y:
            self.rect.y += 1
        elif self.rect.y > player.rect.y:
            self.rect.y -= 1

# Bullet class
class Bullet:
    def __init__(self, x, y, angle, explosive=False):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)
        self.angle = angle
        self.speed = 10
        self.explosive = explosive

    def move(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

    def explode(self, zombies, player, explosions):
        explosion_radius = 100  # Adjust radius as needed
        for zombie in zombies[:]:
            if (self.rect.centerx - explosion_radius <= zombie.rect.centerx <= self.rect.centerx + explosion_radius and
                self.rect.centery - explosion_radius <= zombie.rect.centery <= self.rect.centery + explosion_radius):
                zombies.remove(zombie)  # Remove the zombie
                player.money += MONEY_PER_KILL  # Increase player's money for each zombie killed

        # Create an explosion effect
        explosions.append(Explosion(self.rect.centerx, self.rect.centery))  # Add explosion to the list

# Explosion class
class Explosion:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 100)  # Explosion size
        self.life = 30  # Number of frames the explosion will last

    def update(self):
        self.life -= 1  # Decrease life

    def is_alive(self):
        return self.life > 0

# Shop function
def show_shop(player):
    font = pygame.font.Font(None, 36)
    shop_opened = True

    while shop_opened:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:  # Close shop with Escape key
            shop_opened = False

        if keys[pygame.K_h]:  # Purchase health
            player.purchase_health()
        if keys[pygame.K_f]:  # Upgrade fire rate
            player.upgrade_fire_rate()
        if keys[pygame.K_a]:  # Purchase aimbot
            player.purchase_aimbot()

        # Draw shop
        screen.fill(BLACK)
        health_text = font.render(f'Buy Health (+20) - Cost: ${HEALTH_COST}', True, WHITE)
        fire_rate_text = font.render(f'Upgrade Fire Rate - Cost: ${FIRE_RATE_UPGRADE_COST}', True, WHITE)
        aimbot_text = font.render(f'Purchase Aimbot - Cost: ${AIMBOT_COST}', True, WHITE)
        money_text = font.render(f'Money: ${player.money}', True, WHITE)

        screen.blit(health_text, (WIDTH // 4, HEIGHT // 4))
        screen.blit(fire_rate_text, (WIDTH // 4, HEIGHT // 4 + 40))
        screen.blit(aimbot_text, (WIDTH // 4, HEIGHT // 4 + 80))
        screen.blit(money_text, (10, 10))

        pygame.display.flip()

# Main function
def main():
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    zombies = []
    bullets = []
    explosions = []  # List to hold explosions
    spawn_timer = 0
    last_shot_time = pygame.time.get_ticks()
    wave_number = 0
    wave_start_time = pygame.time.get_ticks()
    zombies_to_spawn = ZOMBIES_PER_WAVE
    explosive_rounds = False
    last_toggle_time = 0  # Track the last toggle time

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            player.move(5, 0)
        if keys[pygame.K_UP]:
            player.move(0, -5)
        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        # Toggle explosive rounds with delay
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_e] and current_time - last_toggle_time >= EXPLOSIVE_TOGGLE_DELAY:
            explosive_rounds = not explosive_rounds
            last_toggle_time = current_time  # Update the last toggle time

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Shooting logic with fire rate
        fire_rate = player.get_fire_rate()

        if player.aimbot_enabled and zombies:
            closest_zombie = min(zombies, key=lambda z: player.rect.centerx - z.rect.centerx)
            if (current_time - last_shot_time) >= fire_rate:
                bullet_x = player.rect.centerx
                bullet_y = player.rect.centery
                target_x = closest_zombie.rect.centerx
                target_y = closest_zombie.rect.centery
                angle = math.atan2(target_y - bullet_y, target_x - bullet_x)
                bullets.append(Bullet(bullet_x, bullet_y, angle, explosive=explosive_rounds))
                last_shot_time = current_time

        elif keys[pygame.K_SPACE] and (current_time - last_shot_time) >= fire_rate:
            bullet_x = player.rect.centerx
            bullet_y = player.rect.centery
            angle = math.atan2(mouse_y - bullet_y, mouse_x - bullet_x)
            bullets.append(Bullet(bullet_x, bullet_y, angle, explosive=explosive_rounds))
            last_shot_time = current_time

        if keys[pygame.K_s]:
            show_shop(player)

        # Wave management
        if len(zombies) < zombies_to_spawn and (current_time - wave_start_time) < WAVE_DURATION * 1000:
            if spawn_timer >= 30:  # Spawn a new zombie every 30 frames
                zombies.append(Zombie())
                spawn_timer = 0
            else:
                spawn_timer += 1
        elif len(zombies) == 0 and (current_time - wave_start_time) >= WAVE_DURATION * 1000:
            wave_number += 1
            zombies_to_spawn += ZOMBIES_PER_WAVE  # Increase zombies per wave
            wave_start_time = current_time

        # Move zombies and check for collisions
        for zombie in zombies[:]:
            zombie.move_towards_player(player)
            if player.rect.colliderect(zombie.rect):
                player.hp -= 1
                zombies.remove(zombie)

        # Move bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
                bullets.remove(bullet)
            for zombie in zombies[:]:
                if bullet.rect.colliderect(zombie.rect):
                    if bullet.explosive:
                        bullet.explode(zombies, player, explosions)  # Explode on impact
                    else:
                        player.money += MONEY_PER_KILL  # Normal bullet hit
                        zombies.remove(zombie)
                    bullets.remove(bullet)  # Remove the bullet after impact
                    break

        # Update explosions
        for explosion in explosions[:]:
            explosion.update()
            if not explosion.is_alive():
                explosions.remove(explosion)

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, player.rect)
        for zombie in zombies:
            pygame.draw.rect(screen, RED, zombie.rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect)

        # Draw explosions
        for explosion in explosions:
            pygame.draw.circle(screen, (255, 255, 0), explosion.rect.center, 50)  # Draw explosion as a yellow circle

        # Draw crosshair
        pygame.draw.circle(screen, WHITE, (mouse_x, mouse_y), 5)

        # Draw HP, Money, and Wave Info
        font = pygame.font.Font(None, 36)
        hp_text = font.render(f'HP: {player.hp}', True, WHITE)
        money_text = font.render(f'Money: ${player.money}', True, WHITE)
        wave_text = font.render(f'Wave: {wave_number}', True, WHITE)
        aimbot_status = "Aimbot: ON" if player.aimbot_enabled else "Aimbot: OFF"
        explosive_status = "Explosive Rounds: ON" if explosive_rounds else "Explosive Rounds: OFF"
        aimbot_text = font.render(aimbot_status, True, WHITE)
        explosive_text = font.render(explosive_status, True, WHITE)

        screen.blit(hp_text, (10, 10))
        screen.blit(money_text, (10, 50))
        screen.blit(wave_text, (10, 90))
        screen.blit(aimbot_text, (10, 130))
        screen.blit(explosive_text, (10, 170))

        pygame.display.flip()
        clock.tick(FPS)

        # End game if HP is zero
        if player.hp <= 0:
            running = False

    pygame.quit()

if __name__ == '__main__':
    main()

