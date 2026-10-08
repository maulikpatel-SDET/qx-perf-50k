"""Service module 48172: business logic, no crypto."""


def calculate_total_48172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48172():
    return 'module 48172 handles orders and invoices'
