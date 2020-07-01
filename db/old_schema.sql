CREATE TABLE `team` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE `tournament` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE `event` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL,
    `tournament_id` INT NOT NULL,
    CONSTRAINT `fk_event_tourname_c3757249` FOREIGN KEY (`tournament_id`) REFERENCES `tournament` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE `address` (
    `city` VARCHAR(64) NOT NULL,
    `street` VARCHAR(128) NOT NULL,
    `event_id` INT NOT NULL  PRIMARY KEY,
    CONSTRAINT `fk_address_event_438f2398` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE `event_team` (
    `event_id` INT NOT NULL,
    `team_id` INT NOT NULL,
    FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`team_id`) REFERENCES `team` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;