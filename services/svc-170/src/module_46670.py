"""Service module 46670: business logic, no crypto."""


def calculate_total_46670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46670():
    return 'module 46670 handles orders and invoices'
