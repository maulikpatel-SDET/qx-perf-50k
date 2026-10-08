"""Service module 36753: business logic, no crypto."""


def calculate_total_36753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36753():
    return 'module 36753 handles orders and invoices'
