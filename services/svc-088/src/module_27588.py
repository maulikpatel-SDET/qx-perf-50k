"""Service module 27588: business logic, no crypto."""


def calculate_total_27588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27588():
    return 'module 27588 handles orders and invoices'
