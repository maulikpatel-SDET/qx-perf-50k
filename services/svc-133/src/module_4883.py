"""Service module 4883: business logic, no crypto."""


def calculate_total_4883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4883():
    return 'module 4883 handles orders and invoices'
