-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `login_reg` ;

-- -----------------------------------------------------
-- Schema login_reg
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `login_reg` DEFAULT CHARACTER SET utf8 ;
USE `login_reg` ;

-- -----------------------------------------------------
-- Table `login_reg`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `login_reg`.`recepis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `login_reg`.`recepis` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(2555) NULL,
  `description` VARCHAR(1200) NULL,
  `instructions` VARCHAR(45) NULL,
  `under_thirty` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`, `users_id`),
  INDEX `fk_recepis_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_recepis_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `login_reg`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
