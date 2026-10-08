"""Service module 27822: business logic, no crypto."""


def calculate_total_27822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27822():
    return 'module 27822 handles orders and invoices'
