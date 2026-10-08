"""Service module 15044: business logic, no crypto."""


def calculate_total_15044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15044():
    return 'module 15044 handles orders and invoices'
