# Car Management API Documentation

## Overview

The Car Management API is a Django application that uses the Django REST Framework to manage a list of cars. This application supports various actions with specific permissions to ensure proper access control.

## Permissions

1. **Create a New Car**
   - **Who Can Create:** Any user
   - **Description:** Any user can create a new car entry in the system.

2. **View Cars**
   - **Who Can View:** Any user
   - **Description:** Any user can view the list of all cars available in the system.

3. **View Car Details**
   - **Who Can View:** Any user
   - **Description:** Any user can view the details of any car in the system.

4. **Update Car**
   - **Who Can Update:** Only the owner
   - **Description:** Only the owner of the car can update the car's details.

5. **Delete Car**
   - **Who Can Delete:** Only the owner
   - **Description:** Only the owner of the car can delete the car from the system.

---

**Prepared by:** Abdullah Qdad  
**Date:** August 5, 2024
