"""Service module 41304: business logic, no crypto."""


def calculate_total_41304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41304():
    return 'module 41304 handles orders and invoices'
