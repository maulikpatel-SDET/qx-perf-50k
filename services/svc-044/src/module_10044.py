"""Service module 10044: business logic, no crypto."""


def calculate_total_10044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10044():
    return 'module 10044 handles orders and invoices'
