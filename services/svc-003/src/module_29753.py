"""Service module 29753: business logic, no crypto."""


def calculate_total_29753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29753():
    return 'module 29753 handles orders and invoices'
