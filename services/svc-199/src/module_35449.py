"""Service module 35449: business logic, no crypto."""


def calculate_total_35449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35449():
    return 'module 35449 handles orders and invoices'
