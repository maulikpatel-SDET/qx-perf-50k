"""Service module 33044: business logic, no crypto."""


def calculate_total_33044(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33044():
    return 'module 33044 handles orders and invoices'
