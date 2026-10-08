"""Service module 31044: business logic, no crypto."""


def calculate_total_31044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31044():
    return 'module 31044 handles orders and invoices'
