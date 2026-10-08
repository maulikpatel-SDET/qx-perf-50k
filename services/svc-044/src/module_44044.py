"""Service module 44044: business logic, no crypto."""


def calculate_total_44044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44044():
    return 'module 44044 handles orders and invoices'
