"""Service module 43588: business logic, no crypto."""


def calculate_total_43588(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43588():
    return 'module 43588 handles orders and invoices'
