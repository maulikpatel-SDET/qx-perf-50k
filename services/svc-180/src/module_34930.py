"""Service module 34930: business logic, no crypto."""


def calculate_total_34930(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34930():
    return 'module 34930 handles orders and invoices'
