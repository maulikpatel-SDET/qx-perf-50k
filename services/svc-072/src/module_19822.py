"""Service module 19822: business logic, no crypto."""


def calculate_total_19822(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19822():
    return 'module 19822 handles orders and invoices'
