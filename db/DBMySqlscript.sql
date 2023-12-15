

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema shaikh
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shaikh
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shaikh` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `shaikh` ;

-- -----------------------------------------------------
-- Table `shaikh`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shaikh`.`patients` (
  `patient_id` INT NOT NULL AUTO_INCREMENT,
  `MRN` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE INDEX `MRN` (`MRN` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2752
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
