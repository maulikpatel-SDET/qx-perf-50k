"""Service module 8890: business logic, no crypto."""


def calculate_total_8890(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8890():
    return 'module 8890 handles orders and invoices'
