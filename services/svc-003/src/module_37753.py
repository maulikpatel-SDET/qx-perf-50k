"""Service module 37753: business logic, no crypto."""


def calculate_total_37753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37753():
    return 'module 37753 handles orders and invoices'
